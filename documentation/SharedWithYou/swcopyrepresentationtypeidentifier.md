# SWCopyRepresentationTypeIdentifier

**Framework**: Shared with You  
**Kind**: var

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let SWCopyRepresentationTypeIdentifier: String
```

#### Discussion

Type identifier for copy representation that signals the system to use the app’s local document version.

Register this as the first open-in-place type identifier on an NSItemProvider when you want the system to load the document’s file URL directly from your app rather than from the file provider. This ensures that users share the most current version of their document, including any unsynced local edits.

```None
        When this type identifier is registered first, also register a "public.file-url" representation
        that provides the local file URL.
```

NSItemProvider *provider = [[NSItemProvider alloc] init]; NSURL *localDocumentURL = [self currentDocumentFileURL]; // Obtain from your document management code

// Step 1: Register SWCopyRepresentationTypeIdentifier as an open-in-place file [provider registerFileRepresentationForTypeIdentifier:SWCopyRepresentationTypeIdentifier fileOptions:NSItemProviderFileOptionOpenInPlace visibility:NSItemProviderRepresentationVisibilityAll loadHandler:^NSProgress * _Nullable(void (^completionHandler)(NSURL * _Nullable, BOOL, NSError * _Nullable)) { completionHandler(localDocumentURL, YES, nil); return nil; }];

// Step 2: Register the public.file-url representation [provider registerObject:localDocumentURL visibility:NSItemProviderRepresentationVisibilityAll];

> **Note**: In a UIDocument subclass, use self.fileURL. In an NSDocument subclass, use self.fileURL. For custom document handling, use whatever property or method provides access to the current file location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcopyrepresentationtypeidentifier)*