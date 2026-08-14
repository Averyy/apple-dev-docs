# shouldArchiveValue(forKey:)

**Framework**: Core Animation  
**Kind**: method

Returns a Boolean value indicating whether the value for a given key should be archived.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func shouldArchiveValue(forKey key: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the specified property should be archived, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The default implementation returns [`true`](https://developer.apple.com/documentation/swift/true). This method is called by the object’s implementation of `encodeWithCoder:`.

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

- [class func defaultValue(forKey: String) -> Any?](caemittercell/defaultvalue(forkey:).md)
  Returns the default value of the property with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemittercell/shouldarchivevalue(forkey:))*