# init(livePhotoEditingInput:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates a Live Photo editing context for the specified editing input.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init?(livePhotoEditingInput livePhotoInput: PHContentEditingInput)
```

```objc
- (instancetype) initWithLivePhotoEditingInput:(PHContentEditingInput *) livePhotoInput;
```

## Return Value

A new Live Photo editing context, or `nil` if the provided content editing input does not represent a Live Photo.

## Discussion

In an app using the Photos framework, you obtain a [`PHContentEditingInput`](../phcontenteditinginput.md) object by calling [`requestContentEditingInput(with:completionHandler:)`](../phasset/requestcontenteditinginput%28with,completionhandler%29.md) method of a [`PHAsset`](../phasset.md) object that you’ve previously fetched.

In a photo editing extension that runs within the Photos app, your extension’s main view controller (which adopts the [`PHContentEditingController`](../../PhotosUI/phcontenteditingcontroller.md) protocol) receives a [`PHContentEditingInput`](../phcontenteditinginput.md) object when the user chooses to edit a Live Photo with your extension.

You can create a Live Photo editing context only from [`PHContentEditingInput`](../phcontenteditinginput.md) object that represents a Live Photo. Use the [`livePhoto`](../phcontenteditinginput/livephoto.md) property of the editing input to verify that it has live Photo content.

## Parameters

- `livePhotoInput`: A content editing input object representing the Live Photo for which to perform editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/init(livephotoeditinginput:))*