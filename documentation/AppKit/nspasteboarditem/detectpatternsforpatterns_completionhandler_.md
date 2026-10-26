# detectPatternsForPatterns:completionHandler:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Determines whether this pasteboard item matches the specified patterns, without notifying the person using the app.

**Availability**:
- macOS 15.4+

## Declaration

```objc
- (void) detectPatternsForPatterns:(NSSet<NSString *> *) patterns completionHandler:(void (^)(NSSet<NSString *> *detectedPatterns, NSError *error)) completionHandler;
```

#### Discussion

This method only gives an indication of whether a pasteboard item matches a particular pattern and doesn’t allow the app to access the item’s contents. As a result, the system doesn’t notify the person using the app about reading the contents of the pasteboard.

The following example shows how to use this method to find email and postal addresses in each item on the pasteboard:

```obj-c
NSArray<NSPasteboardItem*> *items = NSPasteboard.generalPasteboard.pasteboardItems;
__block NSUInteger idx = 0;
for (NSPasteboardItem *item in items) {
    NSUInteger itemIndex = idx++;
    [item
     detectPatternsForPatterns:[NSSet setWithArray:@[NSPasteboardDetectionPatternEmailAddress,
                                                     NSPasteboardDetectionPatternPostalAddress]]
     completionHandler:^(NSSet<NSPasteboardDetectionPattern> *matchedPatterns, NSError *error) {
        if (error) {
            NSLog(@"Item %lu: Error: %@", itemIndex, error);
            return;
        }
        BOOL matchedEmail = [matchedPatterns containsObject:NSPasteboardDetectionPatternEmailAddress];
        BOOL matchedPostal = [matchedPatterns containsObject: NSPasteboardDetectionPatternPostalAddress];
        if (matchedEmail) {
            NSLog(@"Item %lu - Email address(es) detected", itemIndex);
        }
        if (matchedPostal) {
            NSLog(@"Item %lu - Postal address(es) detected", itemIndex);
        }
        if (!matchedEmail && !matchedPostal) {
            NSLog(@"Item %lu - Matched neither email nor postal addresses.", itemIndex);
        }
    }];
}
```

## Parameters

- `patterns`: The patterns to detect on the pasteboard item.
- `completionHandler`: A block that the system invokes after detecting patterns on the pasteboard item. The block receives either a set with the patterns the system finds on the pasteboard item or an error if detection fails.

## See Also

### Detecting patterns and metadata in pasteboard items
- [- detectValuesForPatterns:completionHandler:](./detectvaluesforpatterns_completionhandler_.md)
  Determines whether this pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [- detectMetadataForTypes:completionHandler:](./detectmetadatafortypes_completionhandler_.md)
  Determines available metadata from the specified metadata types for this pasteboard item, without notifying the person using the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditem/detectpatternsforpatterns:completionhandler:)*