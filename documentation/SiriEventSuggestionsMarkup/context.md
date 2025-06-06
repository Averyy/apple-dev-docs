# @context

**Framework**: Siri Event Suggestions Markup  
**Kind**: typealias

The open standard reference for interpreting the markup contents.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Declaration

```swift
string @context
```

#### Overview

For JSON-LD, the `@context` for a reservation should always be `http://schema.org`, as in this example:

```xml
<script type="application/ld+json">{ "@context": "http://schema.org", "@type": "TrainReservation", "reservationId": "ASDF1234" /* more data goes here */ }}</script>
```

For Microdata, provide the URL as part of the `itemtype`, as in this example:

```xml
<section itemscope itemtype="http://schema.org/TrainReservation">
Your reservation
<span itemprop="reservationId">ASDF1234</span>
is confirmed!
/* more data goes here */
</section>
```

## See Also

- [type dateTimeISO8601](datetimeiso8601.md)
  A time and date in the ISO-8601 format.
- [type reservationId](reservationid.md)
  A stable, unique identifier for the reservation.
- [type reservationStatus](reservationstatus.md)
  A string indicating that the reservation has been confirmed or canceled.
- [type URL](url.md)
  The address of a webpage.
- [type telephone](telephone.md)
  A phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/@context)*