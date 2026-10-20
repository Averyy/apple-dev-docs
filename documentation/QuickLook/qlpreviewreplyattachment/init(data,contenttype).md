# init(data:contentType:)

**Framework**: Quick Look  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
init(data: Data, contentType: UTType)
```

```objc
- (instancetype) initWithData:(NSData *) data contentType:(UTType *) contentType;
```

#### Discussion

Create an attachment for html previews by providing the data and mime type of the attachment.

## Parameters

- `data`: The data content of an html preview
- `contentType`: The UTType of the attachment for an html preview


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklook/qlpreviewreplyattachment/init(data:contenttype:))*