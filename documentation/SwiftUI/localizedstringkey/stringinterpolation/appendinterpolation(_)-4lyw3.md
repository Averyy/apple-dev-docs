# appendInterpolation(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Appends a literal string segment to a string interpolation.

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
mutating func appendInterpolation(_ string: String)
```

**Other overloads**:

```swift
@export(implementation)
mutating func appendInterpolation(_ attributedSubstring: AttributedSubstring)
```

```swift
@export(implementation)
mutating func appendInterpolation(_ substring: Substring)
```

```swift
mutating func appendInterpolation(_ attributedString: AttributedString)
```

```swift
mutating func appendInterpolation(_ dates: ClosedRange<Date>)
```

```swift
mutating func appendInterpolation(_ image: Image)
```

```swift
mutating func appendInterpolation(_ interval: DateInterval)
```

```swift
mutating func appendInterpolation(_ resource: LocalizedStringResource)
```

```swift
mutating func appendInterpolation(_ text: Text)
```

```swift
mutating func appendInterpolation<T>(_ value: T) where T : _FormatSpecifiable
```

```swift
@export(implementation)
mutating func appendInterpolation<T>(_ object: T)
```

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

## Parameters

- `string`: The literal string to append.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(_:)-4lyw3)*