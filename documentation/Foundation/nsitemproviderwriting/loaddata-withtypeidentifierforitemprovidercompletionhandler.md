# loadData(withTypeIdentifier:forItemProviderCompletionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Loads data of a particular type, identified by the given UTI.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func loadData(withTypeIdentifier typeIdentifier: String, forItemProviderCompletionHandler completionHandler: @escaping (Data?, (any Error)?) -> Void) -> Progress?
```

#### Return Value

The progress of the data load process.

#### Discussion

When the system calls this method, the `typeIdentifier` parameter is set to one of the elements in the `writableTypeIdentifiersForItemProvider` array.

## Parameters

- `typeIdentifier`: The uniform type identifier (UTI) identifying the type of data to load.
- `completionHandler`: The handler that’s called after the data is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsitemproviderwriting/loaddata(withtypeidentifier:foritemprovidercompletionhandler:))*