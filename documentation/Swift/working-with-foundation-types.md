# Working with Foundation Types

**Framework**: Swift

Use bridged Foundation types in your Swift codebase to work with dates, times, and other values.

#### Overview

When importing the Foundation framework, the Swift overlay provides value types for many bridged reference types. Many other types are renamed or nested to clarify relationships.

##### Prefer Swift Value Types to Bridged Objective C Reference Types

The value types in the table below have the same functionality as their corresponding reference types. Class clusters that include immutable and mutable subclasses, like `NSArray` and `NSMutableArray`, are bridged to a single value type.

| Swift value type | Objective-C reference type |
| --- | --- |
| `AffineTransform` | `NSAffineTransform` |
| `Array` | `NSArray` |
| `Calendar` | `NSCalendar` |
| `CharacterSet` | `NSCharacterSet` |
| `Data` | `NSData` |
| `DateComponents` | `NSDateComponents` |
| `DateInterval` | `NSDateInterval` |
| `Date` | `NSDate` |
| `Decimal` | `NSDecimalNumber` |
| `Dictionary` | `NSDictionary` |
| `IndexPath` | `NSIndexPath` |
| `IndexSet` | `NSIndexSet` |
| `Locale` | `NSLocale` |
| `Measurement` | `NSMeasurement` |
| `Notification` | `NSNotification` |
| Swift numeric types (`Int`, `Float`, and so on) | `NSNumber` |
| `PersonNameComponents` | `NSPersonNameComponents` |
| `Set` | `NSSet` |
| `String` | `NSString` |
| `TimeZone` | `NSTimeZone` |
| `URL` | `NSURL` |
| `URLComponents` | `NSURLComponents` |
| `URLQueryItem` | `NSURLQueryItem` |
| `URLRequest` | `NSURLRequest` |
| `UUID` | `NSUUID` |

When Swift code imports Objective-C APIs, the importer replaces Foundation reference types with their corresponding value types. For this reason, you should almost never need to use a bridged reference type directly in your own code.

If you need the reference semantics that come with the Foundation reference type, you can access it with its original `NS` class name prefix. Cast between a Swift value type and its corresponding reference type by using the `as` keyword.

```swift
let dataValue = Data(base64Encoded: myString)
let dataReference = dataValue as NSData?
```

##### Note Renamed Reference Types

For Foundation types that  bridged to value types, the Swift overlay renames classes and protocols, as well as related enumerations and constants. These types and protocols drop their `NS` prefix, with the following exceptions:

- Classes specific to Objective-C or inherently tied to the Objective-C runtime, like `NSObject`, `NSAutoreleasePool`, `NSException`, and `NSProxy`
- Platform-specific classes, like `NSBackgroundActivity`, `NSUserNotification`, and `NSXPCConnection`

Foundation classes often declare enumeration or constant types. When importing these types, Swift moves them to be nested types of their related types. For example, the `NSJSONReadingOptions` option set is imported as `JSONSerialization.ReadingOptions`.

## See Also

- [Working with Core Foundation Types](working-with-core-foundation-types.md)
  Work directly with memory-managed Core Foundation types in your Swift code, and manually handle retains as needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/working-with-foundation-types)*