# init(question:label:)

**Framework**: PermissionKit  
**Kind**: init

Creates a button that requests permission from parents or guardians to continue using your app after a significant update.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- macOS 26.1+
- visionOS 26.2+

## Declaration

```swift
@MainActor
@preconcurrency init(question: PermissionQuestion<Topic>, @ViewBuilder label: @escaping () -> Label) where Topic == SignificantAppUpdateTopic
```

## Parameters

- `question`: The permission question that describes the significant app update.
- `label`: The view to display inside the button.

## See Also

- [init(question: PermissionQuestion<Topic>, label: () -> Label)](permissionbutton/init(question:label:)-25jfa.md)
  Creates a button that requests permission from parents or guardians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionbutton/init(question:label:)-8291n)*