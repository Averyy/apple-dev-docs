# print(_:to:)

**Framework**: Swift  
**Kind**: method

Prints log messages for all publishing events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func print(_ prefix: String = "", to stream: (any TextOutputStream)? = nil) -> Publishers.Print<Self>
```

#### Return Value

A publisher that prints log messages for all publishing events.

#### Discussion

Use [`print(_:to:)`](optional/publisher-swift.struct/print(_:to:).md) to log messages the console.

In the example below, log messages are printed on the console:

```swift
let integers = (1...2)
cancellable = integers.publisher
   .print("Logged a message", to: nil)
   .sink { _ in }

// Prints:
//  Logged a message: receive subscription: (1..<2)
//  Logged a message: request unlimited
//  Logged a message: receive value: (1)
//  Logged a message: receive finished
```

## Parameters

- `prefix`: A string —- which defaults to empty -— with which to prefix all log messages.
- `stream`: A stream for text output that receives messages, and which directs output to the console by default.  A custom stream can be used to log messages to other destinations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/print(_:to:))*