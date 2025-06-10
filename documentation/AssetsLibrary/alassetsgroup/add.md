# add(_:)

**Framework**: Assets Library  
**Kind**: method

Adds an existing asset to the receiver.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func add(_ asset: ALAsset!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `asset` was added successfully, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The method may fail (return [`false`](https://developer.apple.com/documentation/swift/false)) if the group is not editable, or if the asset could not be added to the group.

You should check the [`isEditable`](alassetsgroup/iseditable.md) property of the group to see if it is possible to add an asset to the group.

## Parameters

- `asset`: The asset to add to the receiver.

## See Also

- [var isEditable: Bool](alassetsgroup/iseditable.md)
  Indicates whether the application can edit the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsgroup/add(_:))*