# add(_:withLabel:)

**Framework**: Address Book  
**Kind**: method

Adds a value and its label to a multivalue list.

**Availability**:
- macOS ?+

## Declaration

```swift
func add(_ value: Any!, withLabel label: String!) -> String!
```

#### Return Value

The new identifier if `value` is added successfully; otherwise, `nil`.

#### Discussion

The `value` argument must be of the correct type. For example, if the receiver is the value for a property of type `kABMultiStringProperty`, then `value` needs to be an NSString object. See [`Property Types`](property_types.md) for a list of supported types in a multivalue list (see descriptions of the `kABMulti...` constants). If either the `value` or the `label` argument is `nil`, this method raises an exception.

This method performs no type checking and will let you add a value whose type does not match the types of the other values in the list. However, if you try to use a multivalue list whose values are not all of the same type, other methods, such as the `ABRecord`  [`setValue(_:forProperty:)`](abrecord-swift.class/setvalue(_:forproperty:).md) method, will return `false` or [`kABErrorInProperty`](kaberrorinproperty.md).

## Parameters

- `value`: The value to add.
- `label`: The label to associate with the value.

## See Also

- [func insert(Any!, withLabel: String!, at: Int) -> String!](abmutablemultivalue/insert(_:withlabel:at:).md)
  Inserts a value and its label at the given index in a multivalue list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmutablemultivalue/add(_:withlabel:))*