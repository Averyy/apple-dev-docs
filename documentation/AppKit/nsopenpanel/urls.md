# urls

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of URLs, each of which contains the fully specified location of a selected file or directory.

**Availability**:
- macOS

## Declaration

```swift
var urls: [URL] { get }
```

```objc
@property (copy, readonly) NSArray<NSURL *> * URLs;
```

#### Discussion

This property contains a valid value when the user selects one item or multiple items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/urls)*