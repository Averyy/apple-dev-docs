# Pausing and resuming uploads

**Framework**: Foundation

Pause and resume an upload without starting over, even when the connection is interrupted.

#### Overview

Your app or a person using it might need to cancel an in-progress upload and resume it later. By supporting resumable uploads, you save both the user’s time and network bandwidth.

New in iOS 17 and aligned OS versions, [`URLSession`](urlsession.md) supports resumable uploads according to the [`latest resumable upload protocol draft`](https://developer.apple.comhttps://www.ietf.org/archive/id/draft-ietf-httpbis-resumable-upload-01.txt). This protocol is currently being developed in the HTTP Working Group at the IETF. To take advantage of resumable uploads, the server you’re connecting to must also support this protocol.

You can use this technique to manually pause and resume an upload, or even resume an upload that failed due to a temporary loss of connectivity. In both cases, [`URLSession`](urlsession.md) needs information on how to resume the upload, which is stored in a `resumeData` object.

##### Pause an Upload

You can effectively pause a [`URLSessionUploadTask`](urlsessionuploadtask.md) by calling [`cancel(byProducingResumeData:)`](urlsessiondownloadtask/cancel(byproducingresumedata:).md). This method cancels the task and passes a `resumeData` parameter to its completion handler. If `resumeData` is not `nil`, you can use this token later to resume the upload. The listing below shows how to cancel an upload task and store `resumeData`, if it exists, in a property:

```swift
uploadTask.cancel { resumeData in
    guard let resumeData else { 
      // The upload can't be resumed; remove the upload from the UI if necessary.
      return
    }
    self.resumeData = resumeData
}
```

> ❗ **Important**:  You can’t resume all uploads. The server must support the [`latest resumable upload protocol draft`](https://developer.apple.comhttps://www.ietf.org/archive/id/draft-ietf-httpbis-resumable-upload-01.txt) from the HTTP Working Group at the IETF. Also, uploads that use a background configuration handle resumption automatically, so manual resuming is only needed for non-background uploads.

##### Recover a Failed Upload

If there’s only a momentary network interruption, but the server is still reachable, [`URLSession`](urlsession.md) automatically tries to resume the upload for you. No extra code is needed.

For broader losses of connectivity, you can resume a failed upload by checking for resume data in the task’s error.

When the upload fails, the session calls your [`urlSession(_:task:didCompleteWithError:)`](urlsessiontaskdelegate/urlsession(_:task:didcompletewitherror:).md) delegate method. If `error` is not `nil`, look in its `userInfo` dictionary for the key [`NSURLSessionUploadTaskResumeData`](nsurlsessionuploadtaskresumedata.md). If the key exists, save the value associated with it to use later when you try to resume the upload. If the key doesn’t exist, you can’t resume the upload.

You can conveniently access resume data using the [`uploadTaskResumeData`](urlerror/uploadtaskresumedata.md) property of [`URLError`](urlerror.md).

You can also catch the error from asynchronous [`URLSession`](urlsession.md) upload methods such as [`upload(for:fromFile:)`](urlsession/upload(for:fromfile:).md). The listing below shows an implementation of this error handling that checks the error for resume data:

```swift
do {
    let (data, response) = try await session.upload(for: request, fromFile: fileURL)
} catch let error as URLError {
    guard let resumeData = error.uploadTaskResumeData else {
        // The upload can't be resumed.
        return
    }
    self.resumeData = resumeData
}
```

##### Resume Uploading

When it’s appropriate to resume the upload, create a new [`URLSessionUploadTask`](urlsessionuploadtask.md) by using the [`uploadTask(withResumeData:)`](urlsession/uploadtask(withresumedata:).md) method of [`URLSession`](urlsession.md), passing in the `resumeData` object you stored earlier. Then, call [`resume()`](urlsessiontask/resume().md) on the task to resume the upload:

```swift
guard let resumeData = self.resumeData else {
    // Inform the user that the upload can't be resumed.
    return
}

let uploadTask = session.uploadTask(withResumeData: resumeData)
uploadTask.resume()
self.uploadTask = uploadTask
```

## See Also

- [Building a resumable upload server with SwiftNIO](building-a-resumable-upload-server-with-swiftnio.md)
  Support HTTP resumable upload protocol in SwiftNIO by translating resumable uploads to regular uploads.
- [Uploading data to a website](uploading-data-to-a-website.md)
  Post data from your app to servers.
- [Uploading streams of data](uploading-streams-of-data.md)
  Send a stream of data to a server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/pausing-and-resuming-uploads)*