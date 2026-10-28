# addProgressReportingCapabilities(_:)

**Framework**: ClassKit  
**Kind**: method  
**Role**: Instance Method

Adds a progress reporting capability to the set of capabilities for the context.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func addProgressReportingCapabilities(_ capabilities: Set<CLSProgressReportingCapability>)
```

```objc
- (void) addProgressReportingCapabilities:(NSSet<CLSProgressReportingCapability *> *) capabilities;
```

## Discussion

Use this method at the time you create a context to indicate what kinds of metrics, like duration, a score, or a binary result, that you record for the context. This helps teachers to understand what to expect when assigning a context.

By default, all contexts have a [`CLSProgressReportingCapability.Kind.duration`](../clsprogressreportingcapability/kind-swift.enum/duration.md) capability, because the framework records duration automatically. But you can add others, according to which metrics you record. You can also add another duration capability, but because a context can have only one capability of a given kind, yours supersedes the default.

To remove all capabilities that you previously added, call the [`resetProgressReportingCapabilities()`](./resetprogressreportingcapabilities%28%29.md) method. This restores the context to its default state, which is to have only the default duration capability.

## See Also

### Indicating progress reporting capabilities
- [var progressReportingCapabilities: Set<CLSProgressReportingCapability>](./progressreportingcapabilities.md)
  The kinds of progress reporting that the context can perform.
- [func resetProgressReportingCapabilities()](./resetprogressreportingcapabilities%28%29.md)
  Resets the set of capabilities for the context.
- [class CLSProgressReportingCapability](../clsprogressreportingcapability.md)
  A progress reporting capability supported by a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/addprogressreportingcapabilities(_:))*