# noteClientStringWillChange()

**Framework**: AppKit  
**Kind**: method

Invoke this method when the searched content will change.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func noteClientStringWillChange()
```

#### Discussion

When incremental search is enabled, this method must be called when it is known that the client’s string will be modified. This method must be called before the client string modification takes place.

## See Also

- [var client: (any NSTextFinderClient)?](nstextfinder/client.md)
  The object that provides the target search string, find bar location, and feedback methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/noteclientstringwillchange())*