# init(contentEditingInput:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates an editing output from the specified editing input.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(contentEditingInput: PHContentEditingInput)
```

```objc
- (instancetype) initWithContentEditingInput:(PHContentEditingInput *) contentEditingInput;
```

#### Return Value

An initialized content editing output.

#### Discussion

To complete the edit, use the [`renderedContentURL`](./renderedcontenturl.md) property to provide the edited asset content. Then, use the [`PHAssetChangeRequest`](../phassetchangerequest.md) class or [`PHContentEditingController`](https://developer.apple.com/documentation/photosui/phcontenteditingcontroller) protocol to commit the edit to storage.

## Parameters

- `contentEditingInput`: An object providing information about the asset to be edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcontenteditingoutput/init(contenteditinginput:))*