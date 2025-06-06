# fileMover(isPresented:file:onCompletion:onCancellation:)

**Framework**: Familycontrols  
**Kind**: method

Presents a system dialog for allowing the user to move an existing file to a new location.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: @escaping (Result<URL, any Error>) -> Void, onCancellation: @escaping () -> Void) -> some View
```

#### Discussion

> **Note**: This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to move a file might look like this:

```swift
  struct MoveFileButton: View {
      @State private var showFileMover = false
      var file: URL
      var onCompletion: (URL) -> Void
      var onCancellation: (() -> Void)?

      var body: some View {
          Button {
              showFileMover = true
          } label: {
              Label("Choose destination", systemImage: "folder.circle")
          }
          .fileMover(isPresented: $showFileMover, file: file) { result in
              switch result {
              case .success(let url):
                  guard url.startAccessingSecurityScopedResource() else {
                      return
                  }
                  onCompletion(url)
                  url.stopAccessingSecurityScopedResource()
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
- `file`: The URL of the file to be moved.
- `onCompletion`: A callback that will be invoked when the operation has   succeeded or failed. The   indicates whether   the operation succeeded or failed. To access the received URLs, call   .   When the access is no longer required, call  .
- `onCancellation`: A callback that will be invoked   if the user cancels the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/filemover(ispresented:file:oncompletion:oncancellation:))*