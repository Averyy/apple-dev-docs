# fileImporter(isPresented:allowedContentTypes:onCompletion:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Presents a system interface for allowing the user to import an existing file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+

## Declaration

```swift
nonisolated
func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: @escaping (Result<URL, any Error>) -> Void) -> some View
```

#### Discussion

In order for the interface to appear, `isPresented` must be `true`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

> **Note**: This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

For example, an application can have a button that allows the user to choose the default directory with document templates loaded on every launch. Such a button might look like this:

```None
 struct PickTemplatesDirectoryButton: View {
     @State private var showFileImporter = false
     var onTemplatesDirectoryPicked: (URL) -> Void

     var body: some View {
         Button {
             showFileImporter = true
         } label: {
             Label("Choose templates directory", systemImage: "folder.circle")
         }
         .fileImporter(
             isPresented: $showFileImporter,
             allowedContentTypes: [.directory]
         ) { result in
              switch result {
              case .success(let directory):
                  // gain access to the directory
                  let gotAccess = directory.startAccessingSecurityScopedResource()
                  if !gotAccess { return }
                  // access the directory URL
                  // (read templates in the directory, make a bookmark, etc.)
                  onTemplatesDirectoryPicked(directory)
                  // release access
                  directory.stopAccessingSecurityScopedResource()
              case .failure(let error):
                  // handle error
                  print(error)
              }
         }
     }
 }
```

> **Note**: Changing `allowedContentTypes` while the file importer is presented will have no immediate effect, however will apply the next time it is presented.

## Parameters

- `isPresented`: A binding to whether the interface should be shown.
- `allowedContentTypes`: The list of supported content types which can   be imported.
- `onCompletion`: A callback that will be invoked when the operation has   succeeded or failed. To access the received URLs, call  .   When the access is no longer required, call  .
- `result`: A   indicating whether the operation succeeded or   failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/fileimporter(ispresented:allowedcontenttypes:oncompletion:))*