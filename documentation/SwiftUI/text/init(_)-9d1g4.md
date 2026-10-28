# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a text view that displays a stored string without localization.

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
init<S>(_ content: S) where S : StringProtocol
```

**Other overloads**:

```swift
init(_ attributedContent: AttributedString)
```

```swift
init(_ dates: ClosedRange<Date>)
```

```swift
init(_ image: Image)
```

```swift
init(_ interval: DateInterval)
```

```swift
init(_ resource: LocalizedStringResource)
```

## Discussion

Use this initializer to create a text view that displays — without localization — the text in a string variable.

```swift
Text(someString) // Displays the contents of `someString` without localization.
```

SwiftUI doesn’t call the `init(_:)` method when you initialize a text view with a string literal as the input. Instead, a string literal triggers the [`init(_:tableName:bundle:comment:)`](./init%28_,tablename,bundle,comment%29.md) method — which treats the input as a [`LocalizedStringKey`](../localizedstringkey.md) instance — and attempts to perform localization.

By default, SwiftUI assumes that you don’t want to localize stored strings, but if you do, you can first create a localized string key from the value, and initialize the text view with that. Using a key as input triggers the [`init(_:tableName:bundle:comment:)`](./init%28_,tablename,bundle,comment%29.md) method instead.

## Parameters

- `content`: The string value to display without localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:)-9d1g4)*