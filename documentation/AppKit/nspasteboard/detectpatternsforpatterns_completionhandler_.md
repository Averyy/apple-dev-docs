# detectPatternsForPatterns:completionHandler:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the first pasteboard item matches the specified patterns, without notifying the person using the app.

**Availability**:
- macOS 15.4+

## Declaration

```objc
- (void) detectPatternsForPatterns:(NSSet<NSString *> *) patterns completionHandler:(void (^)(NSSet<NSString *> *detectedPatterns, NSError *error)) completionHandler;
```

## Discussion

This method only gives an indication of whether the first pasteboard item matches a particular pattern, and doesn’t allow the app to access the item’s contents. As a result, the system doesn’t notify the person using the app about reading the contents of the pasteboard.

The following example shows how to use this method to find email and postal addresses in the first pasteboard item:

```obj-c
[NSPasteboard.generalPasteboard
 detectPatternsForPatterns:[NSSet setWithArray:@[NSPasteboardDetectionPatternEmailAddress,
                                                 NSPasteboardDetectionPatternPostalAddress]]
 completionHandler:^(NSSet<NSPasteboardDetectionPattern> *matchedPatterns, NSError *error) {
    if (error) {
        NSLog(@"Error: %@", error);
        return;
    }
    BOOL matchedEmail = [matchedPatterns containsObject:NSPasteboardDetectionPatternEmailAddress];
    BOOL matchedPostal = [matchedPatterns containsObject: NSPasteboardDetectionPatternPostalAddress];
    if (matchedEmail) {
        NSLog(@"Email address(es) detected");
    }
    if (matchedPostal) {
        NSLog(@"Postal address(es) detected");
    }
    if (!matchedEmail && !matchedPostal) {
        NSLog(@"Matched neither email nor postal addresses.");
    }
}];
```

## Parameters

- `patterns`: The patterns to detect on the pasteboard.
- `completionHandler`: A block the system invokes after detecting patterns on the pasteboard. The block receives either a set with the patterns the system finds on the pasteboard or an error if detection fails.

## See Also

### Detecting patterns and metadata in pasteboard items
- [- detectValuesForPatterns:completionHandler:](./detectvaluesforpatterns_completionhandler_.md)
  Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [Pasteboard detection patterns](../nspasteboard-detection-patterns.md)
  Common types of data that the data detection system matches for a pasteboard.
- [- detectMetadataForTypes:completionHandler:](./detectmetadatafortypes_completionhandler_.md)
  Determines available metadata from the specified metadata types for the first pasteboard item, without notifying the person using the app.
- [Pasteboard detection metadata types](../nspasteboard-detection-metadata-types.md)
  Common types of metadata that the data detection system matches for a pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/detectpatternsforpatterns:completionhandler:)*