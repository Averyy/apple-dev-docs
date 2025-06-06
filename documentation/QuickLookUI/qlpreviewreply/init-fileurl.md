# init(fileURL:)

**Framework**: Quick Look UI  
**Kind**: init

Creates a preview reply from an existing file URL.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(fileURL: URL)
```

#### Discussion

Use [`init(fileURL:)`](qlpreviewreply/init(fileurl:).md) to create a reply from an existing file URL, such as an image or PDF. The following example illustrates creating a reply from an existing URL:

```swift
guard let imageFileURL = Bundle.main.url(forResource: "yourImage", 
                                         withExtension: "jpg") else {
    return
}
let reply = QLPreviewReply(fileURL: imageFileURL)

```

## Parameters

- `fileURL`: The file URL with the content of the reply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewreply/init(fileurl:))*