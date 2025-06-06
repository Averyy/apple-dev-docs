# init(_:)

**Framework**: Swift  
**Kind**: init

Convert this `UnownedJob/Priority` to a [`TaskPriority`](taskpriority.md).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init?(_ p: JobPriority)
```

#### Discussion

Most values are directly interchangeable, but this initializer reserves the right to fail for certain values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskpriority/init(_:))*