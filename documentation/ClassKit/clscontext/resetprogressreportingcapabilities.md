# resetProgressReportingCapabilities()

**Framework**: ClassKit  
**Kind**: method

Resets the set of capabilities for the context.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func resetProgressReportingCapabilities()
```

#### Discussion

Use this method to remove all the capabilities that you previously added with the [`addProgressReportingCapabilities(_:)`](clscontext/addprogressreportingcapabilities(_:).md) method. After calling the reset method, the context reverts to having only the default [`CLSProgressReportingCapability.Kind.duration`](clsprogressreportingcapability/kind-swift.enum/duration.md) capability that it had after initialization.

## See Also

- [var progressReportingCapabilities: Set<CLSProgressReportingCapability>](clscontext/progressreportingcapabilities.md)
  The kinds of progress reporting that the context can perform.
- [func addProgressReportingCapabilities(Set<CLSProgressReportingCapability>)](clscontext/addprogressreportingcapabilities(_:).md)
  Adds a progress reporting capability to the set of capabilities for the context.
- [class CLSProgressReportingCapability](clsprogressreportingcapability.md)
  A progress reporting capability supported by a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/resetprogressreportingcapabilities())*