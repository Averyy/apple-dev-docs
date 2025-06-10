# Siri Event Suggestions Markup

**Framework**: Siri Event Suggestions Markup  
**Kind**: module

Update users’ calendars and inform suggestions from Siri with reservation data embedded in email and webpages.

**Availability**:
- Siri Event Suggestions Markup 1.0+

## Mentions

- [Providing Trusted Data](providing-trusted-data.md)

#### Overview

You can use the Siri Event Suggestions Markup data format to provide event details in webpages and emails. Siri parses travel arrangements, shows, restaurant reservations, and social events in order to augment related activities, like suggesting driving directions or a ride share to a scheduled event and activating Do Not Disturb just before a show starts.

When Mail receives an email or Safari loads a webpage with reservation markup, Siri also adds the event to the user’s Siri Event Suggestions calendar. Mail and Safari also inform the user that the content they’re viewing includes a reservation, so the user can accept or reject the event without leaving their current activity.

![A diagram of the Siri Event Suggestions Markup process, which begins with a graphic representing a piece of reservation data. An arrow points from the reservation graphic to a Siri icon, and from the Siri icon to a calendar, a driving directions graphic, and a Siri Suggestion containing the text “Time to check-in” and “Reservation found in Mail”.](https://docs-assets.developer.apple.com/published/7f308882e351d5cd4cdb42492120db61/media-3672141%402x.png)

Include reservation markup data when you communicate about confirmed reservations with your users. Use a consistent [`reservationId`](reservationid.md) each time, so the system can manage duplicates between Safari and Mail and across the user’s devices.

Fill out the form at [`Siri Event Suggestions Markup Information`](https://developer.apple.comhttps://developer.apple.com/contact/request/siri-events/) to request inclusion in the domain allow list for event suggestion processing. See [`Checking Your Reservation Markup`](checking-your-reservation-markup.md) for more details about testing your implementation before you apply.

> 💡 **Tip**:  Donate reservation information from your app as well, if you have one. For more information about providing event suggestions from your app, see doc://com.apple.documentation/documentation/sirikit/siri_event_suggestions.

##### Format Reservation Data

If you offer reservations on a website or email reservation confirmations to users, you may provide reservation information embedded in HTML documents as either JSON-LD or Microdata. For JSON-LD, specify the [`@context`](@context.md) and `@type,` as shown in this example:

```xml
<script type="application/ld+json">
{
  "@context": "http://schema.org", 
  "@type": "TrainReservation",
  "reservationId": "ASDF1234"
  /* more data goes here */    
}
</script>
```

For Microdata, provide the schema.org URL for the reservation in an `itemtype` attribute like this:

```xml
<section itemscope itemtype="http://schema.org/TrainReservation">
Your reservation
<span itemprop="reservationId">ASDF1234</span>
is confirmed!
/* more data goes here */
</section>
```

## Topics

### Essentials
- [Providing Trusted Data](providing-trusted-data.md)
  Sign your content and avoid sending unnecessary or inaccurate information.
- [Checking Your Reservation Markup](checking-your-reservation-markup.md)
  Preview your reservation event data before the Allow List includes your domain.
### Transportation
- [object FlightReservation](flightreservation.md)
  An airplane flight reservation.
- [object TrainReservation](trainreservation.md)
  A reservation for train travel.
- [object BusReservation](busreservation.md)
  A reservation for bus travel.
- [object BoatReservation](boatreservation.md)
  A reservation for boat travel.
- [object RentalCarReservation](rentalcarreservation.md)
  A reservation to rent a car.
### Food, Lodging, and Events
- [object EventReservation](eventreservation.md)
  A reservation for a movie, sporting event, live show, or other scheduled event.
- [object FoodEstablishmentReservation](foodestablishmentreservation.md)
  A restaurant reservation.
- [object LodgingReservation](lodgingreservation.md)
  A hotel reservation or other booking for a place to stay.
### Common Reservation Data
- [object Person](person.md)
  A passenger, diner, lodging guest, or event attendee.
- [object Ticket](ticket.md)
  Details about a ticket for transportation or an event.
- [object Seat](seat.md)
  The specific location reserved for the passenger.
- [object Organization](organization.md)
  A business, transportation provider, or event organizer.
- [object Place](place.md)
  A business, transportation hub, or event venue.
- [object PostalAddress](postaladdress.md)
  A specific geographic location.
### Basic Data Types
- [type @context](@context.md)
  The open standard reference for interpreting the markup contents.
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

*[View on Apple Developer](https://developer.apple.com/documentation/SiriEventSuggestionsMarkup)*