# UIConfigurationTextAttributesTransformer

**Framework**: UIKit  
**Kind**: typealias  
**Role**: Type Alias

Defines a text transformation that can affect the visual appearance of a string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```c
typedef NSDictionary<NSString *,id> *(^)(NSDictionary<NSString *,id> *) UIConfigurationTextAttributesTransformer;
```

#### Discussion

Use a transformer to affect how your attributed text appears on the UI. You provide a closure when initializing the transformer. Your closure accepts a container with the current text attributes and returns a container with the new text attributes.

```objc
UIConfigurationTextAttributesTransformer transformer;
transformer = ^(NSDictionary<NSAttributedStringKey, id> *incoming) {
    NSMutableDictionary<NSAttributedStringKey, id> *outgoing = [incoming mutableCopy];
    outgoing[NSForegroundColorAttributeName] = [UIColor blackColor];
    outgoing[NSFontAttributeName] = [UIFont boldSystemFontOfSize:20];
    return outgoing;
};
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconfigurationtextattributestransformer-c.typealias)*