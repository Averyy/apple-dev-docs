# url

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The URL from which to load texture data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var url: URL { get set }
```

```objc
@property (nonatomic, copy) NSURL * URL;
```

#### Discussion

Changing a texture’s URL loads data from the new URL, replacing the existing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlurltexture/url)*