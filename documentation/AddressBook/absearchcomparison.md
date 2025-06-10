# ABSearchComparison

**Framework**: Address Book  
**Kind**: typealias

Constants used to specify the type of comparison beingmade.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias ABSearchComparison = CFIndex
```

#### Discussion

These constants are used in a call to the [`ABGroupCreateSearchElement(_:_:_:_:_:)`](abgroupcreatesearchelement(_:_:_:_:_:).md) or [`ABPersonCreateSearchElement(_:_:_:_:_:)`](abpersoncreatesearchelement(_:_:_:_:_:).md) functionto specify the type of comparison being made.

## Topics

### Constants
- [var kABEqual: _ABSearchComparison](kabequal.md)
  Search for elements that are equal to the value.
- [var kABNotEqual: _ABSearchComparison](kabnotequal.md)
  Search for elements that are not equal to thevalue.
- [var kABNotEqualCaseInsensitive: _ABSearchComparison](kabnotequalcaseinsensitive.md)
  Search for elements that are not equal to the value, ignoring case.
- [var kABLessThan: _ABSearchComparison](kablessthan.md)
  Search for elements that are less than thevalue.
- [var kABLessThanOrEqual: _ABSearchComparison](kablessthanorequal.md)
  Search for elements that are less than or equalto the value.
- [var kABGreaterThan: _ABSearchComparison](kabgreaterthan.md)
  Search for elements that are greater than thevalue.
- [var kABGreaterThanOrEqual: _ABSearchComparison](kabgreaterthanorequal.md)
  Search for elements that are greater than orequal to the value.
- [var kABEqualCaseInsensitive: _ABSearchComparison](kabequalcaseinsensitive.md)
  Search for elements that are equal to the value,ignoring case.
- [var kABContainsSubString: _ABSearchComparison](kabcontainssubstring.md)
  Search for elements that contain the value.
- [var kABContainsSubStringCaseInsensitive: _ABSearchComparison](kabcontainssubstringcaseinsensitive.md)
  Search for elements that contain the value,ignoring case.
- [var kABPrefixMatch: _ABSearchComparison](kabprefixmatch.md)
  Search for elements that begin with the value.
- [var kABPrefixMatchCaseInsensitive: _ABSearchComparison](kabprefixmatchcaseinsensitive.md)
  Search for elements that begin with the value, ignoring case.
- [var kABSuffixMatch: _ABSearchComparison](kabsuffixmatch.md)
  Search for elements that end with the value.
- [var kABSuffixMatchCaseInsensitive: _ABSearchComparison](kabsuffixmatchcaseinsensitive.md)
  Search for elements that end with the value, ignoring case.
- [var kABBitsInBitFieldMatch: _ABSearchComparison](kabbitsinbitfieldmatch.md)
  Search for elements that match the bits in ABPersonFlags.
- [var kABDoesNotContainSubString: _ABSearchComparison](kabdoesnotcontainsubstring.md)
  Search for elements that do not contain the value.
- [var kABDoesNotContainSubStringCaseInsensitive: _ABSearchComparison](kabdoesnotcontainsubstringcaseinsensitive.md)
  Search for elements that do not contain the value, ignoring case.
- [var kABWithinIntervalAroundToday: _ABSearchComparison](kabwithinintervalaroundtoday.md)
  Search for elements that are within a time interval (in seconds) forward or backward from today.
- [var kABWithinIntervalAroundTodayYearless: _ABSearchComparison](kabwithinintervalaroundtodayyearless.md)
  Search for elements that are within a time interval (in seconds) forward or backward from this day in any year.
- [var kABNotWithinIntervalAroundToday: _ABSearchComparison](kabnotwithinintervalaroundtoday.md)
  Search for elements that are  within a time interval (in seconds) forward or backward from today.
- [var kABNotWithinIntervalAroundTodayYearless: _ABSearchComparison](kabnotwithinintervalaroundtodayyearless.md)
  Search for elements that are  within a time interval (in seconds) forward or backward from this day in any year.
- [var kABWithinIntervalFromToday: _ABSearchComparison](kabwithinintervalfromtoday.md)
  Search for elements that are within a time interval (in seconds) forward from today.
- [var kABWithinIntervalFromTodayYearless: _ABSearchComparison](kabwithinintervalfromtodayyearless.md)
  Search for elements that are within a time interval (in seconds) forward from this day in any year.
- [var kABNotWithinIntervalFromToday: _ABSearchComparison](kabnotwithinintervalfromtoday.md)
  Search for elements that are  within a time interval (in seconds) forward from today.
- [var kABNotWithinIntervalFromTodayYearless: _ABSearchComparison](kabnotwithinintervalfromtodayyearless.md)
  Search for elements that are  within a time interval (in seconds) forward from this day in any year.

## See Also

- [typealias ABSearchConjunction](absearchconjunction.md)
  Constants used to create compound search elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/absearchcomparison)*