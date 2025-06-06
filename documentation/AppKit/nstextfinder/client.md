# client

**Framework**: AppKit  
**Kind**: property

The object that provides the target search string, find bar location, and feedback methods.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@IBOutlet
unowned(unsafe) var client: (any NSTextFinderClient)? { get set }
```

#### Discussion

The `NSTextFinder` instance class must be associated with a client object that implements the NSTextFinderClient protocol in order to function. The client is responsible for providing the string to be searched, the location for the find bar, and the methods which control feedback to the user about the search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/client)*