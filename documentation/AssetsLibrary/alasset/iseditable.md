# isEditable

**Framework**: Assets Library  
**Kind**: property

Indicates whether the asset is editable.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isEditable: Bool { get }
```

#### Discussion

The property value is [`true`](https://developer.apple.com/documentation/swift/true) if the application is able to edit the asset, and [`false`](https://developer.apple.com/documentation/swift/false) if the application is not able to edit the asset. Applications are only allowed to edit assets that they originally wrote.

## See Also

- [func value(forProperty: String!) -> Any!](alasset/value(forproperty:).md)
  Returns the value for a given property.
- [var original: ALAsset!](alasset/original.md)
  The original version of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/iseditable)*