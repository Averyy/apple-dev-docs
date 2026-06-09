# init(exporting:as:named:sourceLocation:)

**Framework**: Swift Testing  
**Kind**: init

Initialize an instance of this type that encloses the given transferable value.

**Availability**:
- Swift 6.4+
- Xcode 27.0+ (Beta)

## Declaration

```swift
init<T>(exporting transferableValue: T, as contentType: UTType? = nil, named preferredName: String? = nil, sourceLocation: SourceLocation = #_sourceLocation) async throws where AttachableValue == _AttachableTransferableWrapper<T>, T : Transferable
```

#### Discussion

> **Note**: Any error that occurs while exporting `transferableValue`.

Use this initializer to create an instance of [`Attachment`](attachment.md) from a value that conforms to the [`Transferable`](https://developer.apple.comhttps://developer.apple.com/documentation/coretransferable/transferable) protocol.

```swift
let menu = FoodTruck.menu
let attachment = try await Attachment(exporting: menu, as: .pdf)
Attachment.record(attachment)
```

When you call this initializer and pass it a transferable value, it calls [`exported(as:)`](https://developer.apple.comhttps://developer.apple.com/documentation/coretransferable/transferable/exported(as:)) on that value. This operation may take some time, so this initializer suspends the calling task until it is complete.

## Parameters

- `transferableValue`: The value that will be attached to the output of the test run.
- `contentType`: The content type with which to export `transferableValue`. If this argument is `nil`, the testing library calls [`exportedContentTypes(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/coretransferable/transferable/exportedcontenttypes(_:)) on `transferableValue` and uses the first type the function returns that conforms to [`UTType.data`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/data).
- `preferredName`: The preferred name of the attachment to use when saving it. If `nil`, the testing library attempts to generate a reasonable filename for the attached value.
- `sourceLocation`: The source location of the call to this initializer. This value is used when recording issues associated with the attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachment/init(exporting:as:named:sourcelocation:))*