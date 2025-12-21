# shouldArchiveValue(forKey:)

**Framework**: Core Animation  
**Kind**: method

Returns a Boolean indicating whether the value of the specified key should be archived.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func shouldArchiveValue(forKey key: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the specified property should be archived or [`false`](https://developer.apple.com/documentation/Swift/false) if it should not.

#### Discussion

The default implementation returns [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

- [class func defaultValue(forKey: String) -> Any?](calayer/defaultvalue(forkey:).md)
  Specifies the default value associated with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/shouldarchivevalue(forkey:))*