# fileMover(isPresented:files:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents a system dialog for allowing the user to move a collection of existing files to a new location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: @escaping (Result<[URL], any Error>) -> Void) -> some View where C : Collection, C.Element == URL
```

#### Discussion

> **Note**: This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

To further configure the dialog’s appearance and behavior, use these view modifiers: [`fileDialogDefaultDirectory(_:)`](view/filedialogdefaultdirectory(_:).md), [`fileDialogConfirmationLabel(_:)`](view/filedialogconfirmationlabel(_:).md), [`fileDialogMessage(_:)`](view/filedialogmessage(_:).md), [`fileDialogBrowserOptions(_:)`](view/filedialogbrowseroptions(_:).md), [`fileDialogURLEnabled(_:)`](view/filedialogurlenabled(_:).md), [`fileDialogImportsUnresolvedAliases(_:)`](view/filedialogimportsunresolvedaliases(_:).md), and [`fileDialogCustomizationID(_:)`](view/filedialogcustomizationid(_:).md).

In order for the dialog to appear, both `isPresented` must be `true` and `files` must not be empty. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `files`: A collection of `URL`s for the files to be moved.
- `onCompletion`: A callback that will be invoked when the operation has has succeeded or failed. To access the received URLs, call `startAccessingSecurityScopedResource`. When the access is no longer required, call `stopAccessingSecurityScopedResource`. - **result**: A `Result` indicating whether the operation succeeded or failed.

## See Also

- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](view/filemover(ispresented:file:oncompletion:).md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](view/filemover(ispresented:file:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](view/filemover(ispresented:files:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/filemover(ispresented:files:oncompletion:))*