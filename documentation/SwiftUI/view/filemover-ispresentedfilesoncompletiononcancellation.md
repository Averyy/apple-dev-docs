# fileMover(isPresented:files:onCompletion:onCancellation:)

**Framework**: SwiftUI  
**Kind**: method

Presents a system dialog for allowing the user to move a collection of existing files to a new location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: @escaping () -> Void) -> some View where C : Collection, C.Element == URL
```

#### Discussion

> **Note**: This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to move files might look like this:

```swift
  struct MoveFilesButton: View {
      @Binding var files: [URL]
      @State private var showFileMover = false
      var onCompletion: (URL) -> Void
      var onCancellation: (() -> Void)?

      var body: some View {
          Button {
              showFileMover = true
          } label: {
              Label("Choose destination", systemImage: "folder.circle")
          }
          .fileMover(isPresented: $showFileMover, files: files) { result in
              switch result {
              case .success(let urls):
                  urls.forEach { url in
                      guard url.startAccessingSecurityScopedResource() else {
                          return
                      }
                      onCompletion(url)
                      url.stopAccessingSecurityScopedResource()
                  }
              case .failure(let error):
                  print(error)
                  // handle error
              }
          } onCancellation: {
              onCancellation?()
          }
      }
  }
```

## Parameters

- `isPresented`: A binding to whether the dialog should be shown.
- `files`: A collection of URLs for the files to be moved.
- `onCompletion`: A callback that will be invoked when the operation has   succeeded or failed. The   indicates whether   the operation succeeded or failed.   To access the received URLs, call  .   When the access is no longer required, call  .
- `onCancellation`: A callback that will be invoked   if the user cancels the operation.

## See Also

- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](view/filemover(ispresented:file:oncompletion:).md)
  Presents a system interface for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](view/filemover(ispresented:files:oncompletion:).md)
  Presents a system interface for allowing the user to move a collection of existing files to a new location.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](view/filemover(ispresented:file:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move an existing file to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/filemover(ispresented:files:oncompletion:oncancellation:))*