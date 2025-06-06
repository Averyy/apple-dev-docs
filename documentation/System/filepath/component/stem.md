# stem

**Framework**: System  
**Kind**: property

The non-extension portion of this file or directory  component.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var stem: String { get }
```

#### Discussion

Examples:

- `foo.txt => foo`
- `foo.tar.gz => foo.tar`
- `Foo.app => Foo`
- `.hidden => .hidden`
- `..      => ..`


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/component/stem)*