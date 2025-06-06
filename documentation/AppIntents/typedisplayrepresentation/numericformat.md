# numericFormat

**Framework**: App Intents  
**Kind**: property

A string representing a count for the type, e.g. “2 books”.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var numericFormat: LocalizedStringResource?
```

#### Discussion

In your `numericFormat` implementation, use `StringInterpolation` placeholders and provide a `.stringsdict` file with all possible pluralizations for the type, such as “0 books”, “1 book”, and “2 books”.

Example:

```swift
TypeDisplayRepresentation(
    name: LocalizedStringResource("Book"),
    numericFormat: LocalizedStringResource("\(placeholder: .int) books")
)
```

```swift
<dict>
   <key>Book</key>
   <dict>
     <key>NSStringLocalizedFormatKey</key>
     <string>%#@VARIABLE@</string>
     <key>VARIABLE</key>
     <dict>
       <key>NSStringFormatSpecTypeKey</key>
       <string>NSStringPluralRuleType</string>
       <key>one</key>
       <string>Book</string>
       <key>other</key>
       <string>Books</string>
     </dict>
   </dict>
   <key>%lld books</key>
   <dict>
     <key>NSStringLocalizedFormatKey</key>
     <string>%#@count@</string>
     <key>count</key>
     <dict>
       <key>NSStringFormatSpecTypeKey</key>
       <string>NSStringPluralRuleType</string>
       <key>NSStringFormatValueTypeKey</key>
       <string>lld</string>
       <key>zero</key>
       <string>%lld books</string>
       <key>one</key>
       <string>%lld book</string>
       <key>other</key>
       <string>%lld books</string>
     </dict>
   </dict>
 </dict>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/typedisplayrepresentation/numericformat)*