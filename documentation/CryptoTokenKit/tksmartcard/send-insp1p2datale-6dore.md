# send(ins:p1:p2:data:le:)

**Framework**: CryptoTokenKit  
**Kind**: method

Asynchronously sends an APDU command to the smart card.

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
@backDeployed(before: macOS 27.0, iOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
final func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data? = nil, le: Int? = nil) async throws -> (sw: UInt16, response: Data)
```

#### Return Value

A tuple containing the status word (sw) and response data.

#### Discussion

In an async context, Swift prefers this overload over the synchronous `send(ins:p1:p2:data:le:) throws` method. To call the synchronous overload from an async context, use a typed function reference cast: `card.send as (UInt8, UInt8, UInt8, Data?, Int?) throws -> (UInt16, Data)`

> **Note**: `CancellationError` if the task was cancelled before transmission, or an error if the command fails.

## Parameters

- `ins`: Instruction byte of the APDU command.
- `p1`: P1 parameter byte.
- `p2`: P2 parameter byte.
- `data`: Optional command data.
- `le`: Optional expected response length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/send(ins:p1:p2:data:le:)-6dore)*