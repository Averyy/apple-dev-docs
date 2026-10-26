# detectMetadataForTypes:completionHandler:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines available metadata from the specified metadata types for the first pasteboard item, without notifying the person using the app.

**Availability**:
- macOS 15.4+

## Declaration

```objc
- (void) detectMetadataForTypes:(NSSet<NSString *> *) types completionHandler:(void (^)(NSDictionary<NSString *,id> *detectedMetadata, NSError *error)) completionHandler;
```

#### Discussion

This method only gives access to limited types of metadata and doesn’t allow the app to access the contents. As a result, the system doesn’t notify the person using the app about reading the contents of the pasteboard.

For details about the metadata returned for each type, see [`NSPasteboardMetadataType`](../nspasteboardmetadatatype.md).

The following example shows how to use this method to find the content type of a file reference in the first item on the pasteboard:

```obj-c
[NSPasteboard.generalPasteboard
 detectMetadataForTypes:[NSSet setWithArray:@[NSPasteboardMetadataTypeContentType]]
 completionHandler:^(NSDictionary<NSPasteboardMetadataType, id> *metadata, NSError *error) {
    if (error) {
        NSLog(@"Error: %@", error);
        return;
    }
    UTType *contentType = (UTType*)metadata[NSPasteboardMetadataTypeContentType];
    if (contentType) {
        NSLog(@"Content type is: %@", contentType.identifier);
    } else {
        NSLog(@"Couldn't get content type");
    }
}];
```

## Parameters

- `types`: The metadata types to detect on the pasteboard.
- `completionHandler`: A block the system invokes after detecting metadata on the pasteboard. The block receives either a dictionary with the metadata types the system finds on the pasteboard or an error if detection fails. The dictionary keys specify the matched metadata types and the values specify the corresponding metadata.

## See Also

### Detecting patterns and metadata in pasteboard items
- [- detectPatternsForPatterns:completionHandler:](./detectpatternsforpatterns_completionhandler_.md)
  Determines whether the first pasteboard item matches the specified patterns, without notifying the person using the app.
- [- detectValuesForPatterns:completionHandler:](./detectvaluesforpatterns_completionhandler_.md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [Pasteboard detection patterns](../nspasteboard-detection-patterns.md)
  Common types of data that the data detection system matches for a pasteboard.
- [Pasteboard detection metadata types](../nspasteboard-detection-metadata-types.md)
  Common types of metadata that the data detection system matches for a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/detectmetadatafortypes:completionhandler:)*