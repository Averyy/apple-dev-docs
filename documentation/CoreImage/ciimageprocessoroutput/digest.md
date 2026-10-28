# digest

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A 64-bit digest that uniquely describes the contents of the output of a processor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var digest: UInt64 { get }
```

```objc
@property (nonatomic, readonly) uint64_t digest;
```

## Discussion

This digest will change if the graph up to and including the output of the processor changes in any way.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/digest)*