# EntitlementsQuery

**Framework**: LightweightCodeRequirements  
**Kind**: class

A constraint that tests values in the entitlements dictionary associated with a process or code file.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
class EntitlementsQuery
```

#### Overview

Entitlements dictionaries use strings for keys. The value of each key could be a bool, integer, string, array or another dictionary. Arrays are homogenous. Entitlements queries are a chain of operations that allow matching against arbitrarily nested values in the dictionary.

Example entitlements dictionary:

```xml
<dict>
    <key>com.apple.application-identifier</key>
    <string>com.apple.TextEdit</string>
    <key>com.apple.developer.ubiquity-container-identifiers</key>
    <array>
        <string>com.apple.TextEdit</string>
    </array>
    <key>com.apple.private.hid.client.event-dispatch.internal</key>
    <true/>
</dict>
```

Example query to match the first entitlement exactly

```swift
EntitlementsQuery.key("com.apple.application-identifier").matchSingle(com.apple.TextEdit)
```

Example query to match the second entitlement exactly.

```swift
EntitlementsQuery.key("com.apple.developer.ubiquity-container-identifiers").elementAtIndex(0).matchSingle("com.apple.TextEdit")
```

or to match the second entitlement less specifically

```swift
EntitlementsQuery.key("com.apple.developer.ubiquity-container-identifiers").match("com.apple.TextEdit")
```

The following query will detect the presence of the com.apple.private.hid.client.event-dispatch.internal key without checking its value.

```swift
EntitlementsQuery.key("com.apple.private.hid.client.event-dispatch.internal")
```

To match its value add a match() call to the chain.

```swift
EntitlementsQuery.key("com.apple.private.hid.client.event-dispatch.internal").match(true)
```

The following example demonstrate the keyPrefix query.

```swift
EntitlementsQuery.keyPrefix("com.apple.").match(true)
```

The keyPrefix query will match the “com.apple.application-identifier” only. Then the match query will fail because true does not match “com.apple.TextEdit”.

This constraint will cause a matching failure if the process or file being matched does not include entitlements.

## Topics

### Initializers
- [init(from: any Decoder) throws](entitlementsquery/init(from:).md)
  Create a new instance by decoding from the given decoder
### Instance Methods
- [func elementAtIndex(Int64) -> EntitlementsQuery](entitlementsquery/elementatindex(_:).md)
  Match against the specified index (0 based) in an array. Chain additional qualifiers to constrain the value of element.
- [func encode(to: any Encoder) throws](entitlementsquery/encode(to:).md)
  Encodes this value into the given encoder
- [func key(String) -> EntitlementsQuery](entitlementsquery/key(_:)-swift.method.md)
  Match the specified key in a nested dictionary
- [func keyPrefix(String) -> EntitlementsQuery](entitlementsquery/keyprefix(_:)-swift.method.md)
  Match the specified key prefix in a nested dictionary.
- [func match(String) -> EntitlementsQuery](entitlementsquery/match(_:)-5cqvy.md)
  Match the specified string value against a string or an array of strings.
- [func match(Bool) -> EntitlementsQuery](entitlementsquery/match(_:)-5cw98.md)
  Match the specified bool value against a bool value.
- [func match(Int64) -> EntitlementsQuery](entitlementsquery/match(_:)-6msza.md)
  Match the specified Int64 against an integer or array of integers.
- [func matchPrefix(String) -> EntitlementsQuery](entitlementsquery/matchprefix(_:).md)
  Match the specified string prefix against a string value or array.
- [func matchPrefixSingle(String) -> EntitlementsQuery](entitlementsquery/matchprefixsingle(_:).md)
  Match the specified string prefix value against a string value (not an array).
- [func matchSingle(Int64) -> EntitlementsQuery](entitlementsquery/matchsingle(_:)-49kv7.md)
  Match the specified Int64 value against an integer value (not an array).
- [func matchSingle(String) -> EntitlementsQuery](entitlementsquery/matchsingle(_:)-8ggh1.md)
  Match the specified string against a string value (not an array).
- [func matchType(EntitlementsQuery.DataType) -> EntitlementsQuery](entitlementsquery/matchtype(_:).md)
  Matches the specified type against the current element.
### Type Methods
- [static func key(String) -> EntitlementsQuery](entitlementsquery/key(_:)-swift.type.method.md)
  Match against the specified key name at the root of the entitlements dictionary.
- [static func keyPrefix(String) -> EntitlementsQuery](entitlementsquery/keyprefix(_:)-swift.type.method.md)
  Match the specified key prefix at the root of the entitlements dicitonary. Chain additional qualifiers to constrain the value of the key.
### Enumerations
- [EntitlementsQuery.DataType](entitlementsquery/datatype.md)
  The types of elements allowed in entitlements dictionaries.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [LaunchConstraint](launchconstraint.md)
- [OnDiskConstraint](ondiskconstraint.md)
- [ProcessConstraint](processconstraint.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CodeDirectoryHash](codedirectoryhash.md)
  A constraint that matches the hash of a code directory of a code file or of a running or launching process.
- [struct InfoPlistHash](infoplisthash.md)
  A constraint that tests the specified hash against the Information property list hash stored in the code signature of the process or code file.
- [struct IsInitProcess](isinitprocess.md)
  A constraint that tests whether a process is the operating system’s initial process.
- [struct IsMainBinary](ismainbinary.md)
  A constraint that tests whether a code file is a main binary.
- [struct IsSIPProtected](issipprotected.md)
  A constraint that tests whether a code file or process is on a volume protected by System Integrity Protection (SIP).
- [struct PlatformType](platformtype.md)
  A constraint that tests whether a code file or running process targets a given platform.
- [struct SigningIdentifier](signingidentifier.md)
  A constraint that tests whether the provided signing identifier matches the signature attached to the code.
- [struct TeamIdentifier](teamidentifier.md)
  A constraint that tests whether the provided team identifier matches the team identified in the code signature.
- [struct ValidationCategory](validationcategory.md)
  A constraint that tests whether a code file or running process is signed in a way that conforms to the specified validation category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/lightweightcoderequirements/entitlementsquery)*