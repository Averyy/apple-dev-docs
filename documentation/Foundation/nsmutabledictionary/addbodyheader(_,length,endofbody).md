# addBodyHeader(_:length:endOfBody:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.0+

## Declaration

```swift
func addBodyHeader(_ inHeaderData: UnsafeRawPointer!, length inHeaderDataLength: UInt32, endOfBody isEndOfBody: Bool) -> OBEXError
```

```objc
- (OBEXError) addBodyHeader:(const void *) inHeaderData length:(uint32_t) inHeaderDataLength endOfBody:(BOOL) isEndOfBody;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/addbodyheader(_:length:endofbody:))*