# AppClipAdvancedExperience.Attributes.Place

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The place information of an advanced App Clip experience.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object AppClipAdvancedExperience.Attributes.Place
```

## Mentions

- [App Store Connect API 4.0 release notes](../../app-store-connect-api-4-0-release-notes.md)
- [App Store Connect API 4.2 release notes](../../app-store-connect-api-4-2-release-notes.md)

## Topics

### Objects
- [object AppClipAdvancedExperience.Attributes.Place.DisplayPoint](./place-data.dictionary/displaypoint-data.dictionary.md)
  A point-based representation of a place in Apple Maps.
- [object AppClipAdvancedExperience.Attributes.Place.MainAddress](./place-data.dictionary/mainaddress-data.dictionary.md)
  The main address for a point of interest or business in Apple Maps.
- [object AppClipAdvancedExperience.Attributes.Place.PhoneNumber](./place-data.dictionary/phonenumber-data.dictionary.md)
  The phone number of a point of interest or business in Apple Maps.

## Properties

- `categories` ([string]): A list of categories for a place in Apple Maps you associate with the Advanced App Clip experience.
- `displayPoint` (AppClipAdvancedExperience.Attributes.Place.DisplayPoint): Coordinates of a place in Apple Maps you associate with an advanced App Clip experience.
- `homePage` (string): The optional website URL for a place.
- `mainAddress` (AppClipAdvancedExperience.Attributes.Place.MainAddress): The main address of a place in Apple Maps. This value is required if you don’t provide coordinates for a place.
- `mapAction` (string): A string that describes the intent behind an App Clip invocation from location-based suggestions from Siri Suggestions and the Maps app.

  **Allowed Values**: `BUY_TICKETS`, `VIEW_AVAILABILITY`, `VIEW_PRICING`, `HOTEL_BOOK_ROOM`, `PARKING_RESERVE_PARKING`, `RESTAURANT_JOIN_WAITLIST`, `RESTAURANT_ORDER_DELIVERY`, `RESTAURANT_ORDER_FOOD`, `RESTAURANT_ORDER_TAKEOUT`, `RESTAURANT_RESERVATION`, `SCHEDULE_APPOINTMENT`, `RESTAURANT_VIEW_MENU`, `THEATER_NOW_PLAYING`, `AIRLINE_BOOK_TRAVEL`, `AIRLINE_CHECK_IN`, `AIRLINE_FLIGHT_STATUS`, `APPLY`, `BOOK`, `BOOK_ACTIVITIES`, `BOOK_RIDES`, `BOOK_TEETIMES`, `BOOK_TOURS`, `CAREERS`, `CHARGE_EV`, `COUPONS`, `DONATE`, `EVENTS`, `EVENTS_SHOWS`, `EVENTS_SPORTS`, `GIFT_CARD`, `HOTEL_AMENITIES`, `JOIN`, `PARKING_AVAILABLE`, `RESTAURANT_PICKUP`, `RETAIL_SERVICE_QUOTE`, `RETAIL_STORE_DELIVERY`, `RETAIL_STORE_PICKUP`, `RETAIL_STORE_SHOP`, `SERVICES`, `SUPPORT`, `PAY_TO_PARK`
- `names` ([string]): An array of names as strings for a place in Apple Maps.
- `phoneNumber` (AppClipAdvancedExperience.Attributes.Place.PhoneNumber): The phone number that’s associated with a place in Apple Maps as a string.
- `placeId` (string): An opaque ID that uniquely identifies a place. If you previously created a place in Apple Maps for the place you associate with your advanced App Clip experience, use its ID instead of creating a new ID.
- `relationship` (string): A navigational link to related data and included resource types and IDs.

  **Allowed Values**: `OWNER`, `AUTHORIZED`, `OTHER`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipadvancedexperience/attributes-data.dictionary/place-data.dictionary)*