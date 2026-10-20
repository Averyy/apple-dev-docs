# shouldRunSavePanelWithAccessoryView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document’s Save panel displays a list of supported writable document types.

**Availability**:
- macOS 10.0+ - Deprecated in 27.0

## Declaration

```swift
var shouldRunSavePanelWithAccessoryView: Bool { get }
```

```objc
@property (readonly) BOOL shouldRunSavePanelWithAccessoryView;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the document includes a pop-up menu of supported writable document types when it displays the Save panel. The default value of this property is [`true`](../../Swift/true.md). Subclasses can override this property to provide a different value. For example, you might provide the following implementation:

```objc
- (BOOL)shouldRunSavePanelWithAccessoryView {
    return [self fileURL] == nil;
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/shouldrunsavepanelwithaccessoryview)*