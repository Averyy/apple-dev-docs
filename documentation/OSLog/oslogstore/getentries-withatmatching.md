# getEntries(with:at:matching:)

**Framework**: OSLog  
**Kind**: method

Returns a sequence of log entries filtered by the parameters passed in.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func getEntries(with options: OSLogEnumerator.Options = [], at position: OSLogPosition? = nil, matching predicate: NSPredicate? = nil) throws -> AnySequence<OSLogEntry>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogstore/getentries(with:at:matching:))*