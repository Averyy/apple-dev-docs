# DeviceActivityReport

**Framework**: DeviceActivity  
**Kind**: struct

A view that reports the user’s application, category, and web domain activity in a privacy-preserving way.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
@MainActor
@preconcurrency struct DeviceActivityReport
```

#### Overview

When you create a report, the system asks your app’s device activity report extension to provide a [`View`](https://developer.apple.com/documentation/SwiftUI/View) representing the user’s device activity. To protect the user’s privacy, your extension runs in a sandbox. This sandbox prevents your extension from making network requests or moving sensitive content outside the extension’s address space. The extension point identifier for all device activity report extensions is `com.apple.deviceactivityui.report-extension`. You can configure a report with a custom context and filter, and then display the report like any SwiftUI view.

```swift
struct ExampleView: View {
    let selectedApps: Set<ApplicationToken>
    let selectedCategories: Set<ActivityCategoryToken>
    let selectedWebDomains: Set<WebDomainToken>

    @State private var context: DeviceActivityReport.Context = .barGraph
    @State private var filter = DeviceActivityFilter(
        segment: .daily(
            during: Calendar.current.dateInterval(
               of: .weekOfYear, for: .now
            )!
        ),
        users: .children,
        devices: .init([.iPhone, .iPad]),
        applications: selectedApps,
        categories: selectedCategories,
        webDomains: selectedWebDomains
    )

    public var body: some View {
        VStack {
            DeviceActivityReport(context, filter: filter)

            // A picker used to change the report's context.
            Picker(selection: $context, label: Text("Context: ")) {
                Text("Bar Graph")
                    .tag(DeviceActivityReport.Context.barGraph)
                Text("Pie Chart")
                     .tag(DeviceActivityReport.Context.pieChart)
            }

            // A picker used to change the filter's segment interval.
            Picker(
                selection: $filter.segmentInterval,
                 label: Text("Segment Interval: ")
            ) {
                Text("Hourly")
                    .tag(DeviceActivityFilter.SegmentInterval.hourly())
                Text("Daily")
                    .tag(DeviceActivityFilter.SegmentInterval.daily(
                        during: Calendar.current.dateInterval(
                             of: .weekOfYear, for: .now
                        )!
                    ))
                Text("Weekly")
                    .tag(DeviceActivityFilter.SegmentInterval.weekly(
                        during: Calendar.current.dateInterval(
                            of: .month, for: .now
                        )!
                    ))
            }
            // ...
        }
    }
}
```

The system will only provide your extension with device activity data if the user has authorized your app for family controls on their device or on the device(s) of children in their iCloud family. See [`AuthorizationCenter`](https://developer.apple.com/documentation/FamilyControls/AuthorizationCenter) for more details.

## Topics

### Structures
- [DeviceActivityReport.Context](deviceactivityreport/context.md)
  A context indicating how your device activity report extension should configure its `DeviceActivityReportView`.
### Initializers
- [init(DeviceActivityReport.Context, filter: DeviceActivityFilter)](deviceactivityreport/init(_:filter:).md)
  Creates a new device activity report.
### Instance Properties
- [var body: some View](deviceactivityreport/body.md)
  The content of the device activity report.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport)*