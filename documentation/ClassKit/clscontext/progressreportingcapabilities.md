# progressReportingCapabilities

**Framework**: ClassKit  
**Kind**: property  
**Role**: Instance Property

The kinds of progress reporting that the context can perform.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var progressReportingCapabilities: Set<CLSProgressReportingCapability> { get }
```

```objc
@property (nonatomic, copy, readonly) NSSet<CLSProgressReportingCapability *> * progressReportingCapabilities;
```

## Discussion

Use progress reporting capabilities to tell teachers what kinds of metrics — like duration, percentage completion, or a score — that a context records.

By default, all contexts have a [`CLSProgressReportingCapability.Kind.duration`](../clsprogressreportingcapability/kind-swift.enum/duration.md) capability, because the framework automatically measures time spent on activities —– the time between when you call the [`start()`](../clsactivity/start%28%29.md) and [`stop()`](../clsactivity/stop%28%29.md) methods. You can add one or more other capabilities using the [`addProgressReportingCapabilities(_:)`](./addprogressreportingcapabilities%28_%29.md) method, corresponding to the other kinds of activity that you report for a context. For example, if you set the [`progress`](../clsactivity/progress.md) property of an activity, add the [`CLSProgressReportingCapability.Kind.percent`](../clsprogressreportingcapability/kind-swift.enum/percent.md) capability. Typically, you perform this configuration when creating the context.

The values that you put in the progress reporting capability set don’t affect your ability to record metrics. But they do affect the presentation of your app in the Schoolwork app.

To revert to the default state of reporting only duration, call the [`resetProgressReportingCapabilities()`](./resetprogressreportingcapabilities%28%29.md) method.

## See Also

### Indicating progress reporting capabilities
- [func addProgressReportingCapabilities(Set<CLSProgressReportingCapability>)](./addprogressreportingcapabilities%28_%29.md)
  Adds a progress reporting capability to the set of capabilities for the context.
- [func resetProgressReportingCapabilities()](./resetprogressreportingcapabilities%28%29.md)
  Resets the set of capabilities for the context.
- [class CLSProgressReportingCapability](../clsprogressreportingcapability.md)
  A progress reporting capability supported by a context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clscontext/progressreportingcapabilities)*