# Defining launch environment and library constraints

**Framework**: Security

Restrict your app’s components to their expected contexts.

#### Overview

You define launch environment and library constraints in constraint dictionaries that you either save in `launchd` property list files, or in separate property list files that you use in code signing. The constraint dictionaries you create contain  and . Facts are assertions that properties of the executable the operating system is launching, or the library your process is loading, match conditions you specify. Operations allow for rich combinations of facts.

The top level of a constraint dictionary is implicitly an `$and` operation that includes all of the facts and operations in the dictionary. When one process tries to launch another process — by calling `execve(_:_:_:)` or `posix_spawn(_:_:_:_:_:_:)` — the operating system checks that the executable file satisfies its own self constraint. It also checks that the parent process’s executable satisfies the executable’s parent constraint, and that the responsible process’s executable satsifies the executable’s responsible process constraint. If any of these launch constraints aren’t satisfied, the operating system doesn’t run the program.

Your process can load a dynamic library if all of the facts and operations at the top level of the library constraint dictionary are true for the file that contains the library. If any part of the library constraint isn’t true, your process doesn’t load the library.

`launchd` tests constraints that you specify in `launchd` property list files when it needs to start your launch daemon or agent. If the executable specified in the `launchd` property list doesn’t satisfy the constraint in the property list, then `launchd` doesn’t start the process.

##### Constrain the Executables Launch Environment

Construct the launch constraint by adding keys and values that represent constraint facts, and operators that combine facts using logical operations. Use facts from the list below in your launch constraint.

A single executable file can contain multiple code directory hashes, for different CPU architectures and hash algorithms. Identify an executable’s code directory hash using a collection of valid hashes and the `$in` operation.

Team identifiers are present in executables signed by code signing identities for development, TestFlight, App Store, or Developer ID.

Use values from the table below with the `validation-category` fact.

| Code signature validation category | Description |
| --- | --- |
| `1` | An operating system executable. |
| `2` | An executable distributed through TestFlight. |
| `3` | An executable signed by a development code signing identity. |
| `4` | An executable distributed through the App Store. |
| `5` | An executable distributed using an Enterprise Universal Provisioning Profile, or ad-hoc distribution. |
| `6` | An executable signed using Developer ID. |
| `7`, `8`, or `9` | These values aren’t appropriate for `validation-category` facts in constraints as they represent categories of binaries that the system generates in certain restricted situations. |
| `10` | An executable signed with a code signing identity that doesn’t match any other category. |

This example of a launch constraint uses a `team-identifier` fact to require that an executable’s signed with the Team ID `8XCUU22SN2`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>team-identifier</key>
  <string>8XCUU22SN2</string>
</dict>
</plist>
```

##### Build Complex Checks with Operators

Constraint dictionaries can include any of the following operators, to build complex checks. An operator can take the place of a value in a fact, in which case each of the values in the operator expression applies to the fact that contains the operator. An operator can also take the place of the fact key itself, in which case the values of the operator expression are themselves key-value pairs that name facts. As dictionaries only contain one instance of any particular key, use operators to compose multiple tests that use the same fact.

| Operator | Value type | Description |
| --- | --- | --- |
| `$and` | A dictionary of facts or operators. | An `$and` operation is true if every subexpression is true. |
| `$and-array` | An array of subarrays. Each subarray contains a logical operator (`$and`, `$or`, or `$optional`) followed by a dictionary of facts or operations. | An `$and-array` operation is true if every subexpression is true. Use `$and-array` to simplify expressions that need multiple levels of nesting using `$and`. |
| `$or` | A dictionary of facts or operators. | An `$or` operation is true if any subexpression is true. |
| `$or-array` | An array of subarrays. Each subarray contains a logical operator (`$and`, `$or`, or `$optional`) followed by a dictionary of facts or operations. | An `$or-array` operation is true if any subexpression is true. Use `$or-array` to simplify expressions that need multiple levels of nesting using `$or`. |
| `$in` | A list of strings, data, or integers. | A fact using the `$in` operator is true if the fact’s value is a member of the list. |
| `$lt` | An integer. | A fact using the `$lt` operator is true if the fact’s value is less than the specified value. |
| `$lte` | An integer. | A fact using the `$lte` operator is true if the fact’s value is less than or equal to the specified value. |
| `$gt` | An integer. | A fact using the `$gt` operator is true if the fact’s value is greater than the specified value. |
| `$gte` | An integer. | A fact using the `$gte` operator is true if the fact’s value is greater than or equal to the specified value. |
| `$optional` | A dictionary that contains a single fact or operator. | The result of the `$optional` operator depends on the context of the operator. Inside `$or` and `$or-array` operators, `$optional` is true only if the fact or operator it contains is true. In all other contexts — including inside `$and` or `$and-array` operators — `$optional` is true if the value of the fact or operator it contains is true, or when the value is indeterminate. |
| `$query` | An array that contains subarrays for representing the entitlements query. | The kernel uses the query to test the executable’s entitlements. You can only use a `$query` operator as the value of an `entitlements` fact. To understand the operators and values that you can use in an entitlements query, see Construct an entitlements query below. |

The launch constraint in the example below uses the `$or` operator to require that an executable’s either signed with the Team ID `8XCUU22SN2`, or is an operating system executable.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>$or</key>
  <dict>
    <key>team-identifier</key>
    <string>8XCUU22SN2</string>
    <key>validation-category</key>
    <integer>1</integer>
  </dict>
</dict>
</plist>
```

##### Construct an Entitlements Query

An entitlements query is an array of query operations. Each operation is an array with two entries: an integer operation code, and a parameter that can be an integer, a string, or a Boolean value. The operations either select specific information about the entitlements, or match the currently-selected information against a value specified in the parameter.

The kernel executes your query in a virtual machine (VM) that has a context that includes an entitlements state and a validity flag. The initial value of the state is the executable’s entitlements dictionary, and the query execution is valid. The VM processes each operation in the query in sequence. A select operation updates the state by fetching specific information from the current state, or marks the execution as invalid if it can’t find the requested information. A match operation marks the execution as valid if the current state’s value matches the operation’s parameter, and invalid otherwise. If the execution remains valid until the VM executes all of the operations in the query, then the executable satisfies the query.

Use the following operation codes in entitlements queries:

| Operation code | Operation | Value type | Description |
| --- | --- | --- | --- |
| `1` | Select key | A string that names a dictionary key | If the current state is a dictionary that contains this key, the operation updates the state to the value in the dictionary for the key. If the current state isn’t a dictionary or doesn’t contain the key, the operation marks the query execution as invalid. |
| `2` | Select index | An integer that represents an array index | If the current state is an array with enough elements, the operation updates the state to the value in the array at the given index. If the index isnʼt in the array or the current state isnʼt an array, the operation marks the query execution as invalid. |
| `3` | Match string | A string | Marks the execution as valid if the current state is a string equal to the parameter; otherwise, it’s invalid. |
| `4` | Match string prefix | A string | Marks the execution as valid if the current state is a string that starts with the parameter; otherwise, it’s invalid. |
| `5` | Match Boolean | A Boolean value | Marks the execution as valid if the current state is a Boolean value equal to the parameter; otherwise, it’s invalid. |
| `6` | String value allowed | A string | If the current state is a string, this operation is equivalent to match string (Operation code `3`, above). If the current state is a list of strings, mark the execution as valid if any element in the list if equal to the parameter. |
| `7` | Match integer | An integer | Marks the execution as valid if the current state is an integer equal to the parameter; otherwise, it’s invalid. |
| `8` | String prefix value allowed | A string | If the current state is a string, this operation is equivalent to match string prefix (Operation code `4`, above). If the current state is a list of strings, mark the execution as valid if any element in the list is equal to the parameter. |
| `9` | Select key with prefix | A string that names a dictionary key | If the current state is a dictionary that contains any key starting with the parameter, the operation updates the state to the value in the dictionary for the longest-matching key. If the current state isn’t a dictionary or doesn’t contain a key with the prefix, the operation marks the query execution as invalid. |
| `10` | Integer value allowed | An integer | If the current state is an integer, this operation is equivalent to match integer (Operation code `7`, above). If the current state is a list of integers, mark the execution as valid if any element in the list is equal to the parameter. |
| `11` | Match type | An integer, with values from the table below. | Marks the execution as valid if the type of the current state matches the type specified in the parameter; otherwise, it’s invalid. |

When you write an entitlements `$query` using the match type operation (Operation code 11 in the table above), use one of the values in this table as the parameter:

| Value | The context’s expected type |
| --- | --- |
| 1 | A dictionary |
| 2 | An array |
| 3 | An integer |
| 4 | A string |
| 5 | A Boolean value |

The launch constraint in the example below uses an `entitlements` fact and the `$query` operator to require that an executable has the [`Camera entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.device.camera) (`com.apple.security.device.camera`) with the Boolean value `true`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>entitlements</key>
  <dict>
    <key>$query</key>
    <array>
      <array>
        <integer>1</integer>
        <string>com.apple.security.device.camera</string>
      </array>
      <array>
        <integer>5</integer>
        <true/>
      </array>
    </array>
  </dict>
</dict>
</plist>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/defining-launch-environment-and-library-constraints)*