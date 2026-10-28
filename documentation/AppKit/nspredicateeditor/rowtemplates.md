# rowTemplates

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The row templates for the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var rowTemplates: [NSPredicateEditorRowTemplate] { get set }
```

```objc
@property (copy) NSArray<NSPredicateEditorRowTemplate *> * rowTemplates;
```

## Discussion

The default value is a single compound [`NSPredicateEditorRowTemplate`](../nspredicateeditorrowtemplate.md) object.

## See Also

### Managing Row Templates
- [class NSPredicateEditorRowTemplate](../nspredicateeditorrowtemplate.md)
  A template that describes available predicates and how to display them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspredicateeditor/rowtemplates)*