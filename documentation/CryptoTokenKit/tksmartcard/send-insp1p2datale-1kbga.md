# send(ins:p1:p2:data:le:)

**Framework**: CryptoTokenKit  
**Kind**: method

Synchronously sends an APDU command to the smart card.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data? = nil, le: Int? = nil) throws -> (sw: UInt16, response: Data)
```

#### Return Value

A tuple containing the status word (sw) and response data.

#### Discussion

Use this method when you need synchronous execution, such as within `withSession` blocks or when calling from synchronous code paths.

> **Note**: An error if the command fails.

## Parameters

- `ins`: Instruction byte of the APDU command.
- `p1`: P1 parameter byte.
- `p2`: P2 parameter byte.
- `data`: Optional command data.
- `le`: Optional expected response length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/send(ins:p1:p2:data:le:)-1kbga)*