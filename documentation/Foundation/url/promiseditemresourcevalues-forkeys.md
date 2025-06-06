# promisedItemResourceValues(forKeys:)

**Framework**: Foundation  
**Kind**: method

Gets resource values from URLs of ‘promised’ items.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func promisedItemResourceValues(forKeys keys: Set<URLResourceKey>) throws -> URLResourceValues
```

#### Discussion

A promised item is not guaranteed to have its contents in the file system until you use `FileCoordinator` to perform a coordinated read on its URL, which causes the contents to be downloaded or otherwise generated. Promised item URLs are returned by various APIs, including currently: NSMetadataQueryUbiquitousDataScope NSMetadataQueryUbiquitousDocumentsScope A `FilePresenter` presenting the contents of the directory located by -URLForUbiquitousContainerIdentifier: or a subdirectory thereof

The following methods behave identically to their similarly named methods above (`func resourceValues(forKeys:)`, etc.), except that they allow you to get resource values and check for presence regardless of whether the promised item’s contents currently exist at the URL. You must use these APIs instead of the normal URL resource value APIs if and only if any of the following are true: You are using a URL that you know came directly from one of the above APIs You are inside the accessor block of a coordinated read or write that used NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly, NSFileCoordinatorWritingForDeleting, NSFileCoordinatorWritingForMoving, or NSFileCoordinatorWritingContentIndependentMetadataOnly

Most of the URL resource value keys will work with these APIs. However, there are some that are tied to the item’s contents that will not work, such as `contentAccessDateKey` or `generationIdentifierKey`. If one of these keys is used, the method will return a `URLResourceValues` value, but the value for that property will be nil.

## See Also

- [func checkPromisedItemIsReachable() throws -> Bool](url/checkpromiseditemisreachable.md)
  Returns whether the promised item URL’s resource exists and is reachable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/promiseditemresourcevalues(forkeys:))*