# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object that acts as the delegate of the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
weak var delegate: (any NSScrubberDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSScrubberDelegate> delegate;
```

## See Also

### Configuring the scrubber
- [var dataSource: (any NSScrubberDataSource)?](./datasource.md)
  The object that provides the data for the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/delegate)*