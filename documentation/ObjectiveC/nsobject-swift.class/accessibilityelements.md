# accessibilityElements

**Framework**: Objective-C Runtime  
**Kind**: property

An array of features of an object that assistive technologies can access.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var accessibilityElements: [Any]? { get set }
```

#### Discussion

Set this property on an [`NSObject`](nsobject-swift.class.md) subclass to supplement the default accessibility element hierarchy with elements that you want assistive technologies — such as VoiceOver, Switch Control, and Voice Control — to interact with. In the array your implementation returns, you can include elements such as user interface controls, text, images, or custom accessibility elements that you want to make accessible.

The system adds default accessibility elements to view hierarchies that you build using system-provided UI. However, use this property when you need to make a custom view accessible in ways the system can’t automatically provide. For example, a pie chart that renders using Core Graphics can expose each slice of its chart as a separate accessibility element:

```swift
// A pie chart that implements custom Core Graphics rendering. 
class PieChartView: UIView {
    var slices: [Slice] = []
    // Create accessibility elements. 
    func updateAccessibility() {
        isAccessibilityElement = false
        // Iterate over the chart slices. 
        accessibilityElements = slices.map { slice in
            // Instantiate a custom accessibility element for the slice. 
            let element = UIAccessibilityElement(accessibilityContainer: self)
            element.accessibilityLabel = slice.label
            element.accessibilityValue = "\(slice.percentage)%"
            return element
        }
    }
    // Refresh when the data changes.
    func updateData(_ newSlices: [Slice]) {
        slices = newSlices
        updateAccessibility() 
    }
} 
```

This makes the pie chart data available to assistive technologies. For example, VoiceOver can swipe through the chart slices individually, announcing each slice’s label and percentage value rather than providing only a single, uninformative description for the entire chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityelements)*