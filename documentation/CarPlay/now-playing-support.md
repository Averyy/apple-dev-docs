# Now Playing supporting types

**Framework**: CarPlay  
**Role**: API Collection

Add Now Playing buttons to your interface and configure overlays with sports information.

## Overview

Display the standard buttons in your Now Playing interface. If your app manages sports-related content, display scores directly from the Now Playing interface. Display this information with audio from the match or on its own as the game progresses.

## Topics

### Interface modes
- [class CPNowPlayingModeSports](./cpnowplayingmodesports.md)
  A mode that manages the sporting event details to display in the Now Playing interface.
- [class CPNowPlayingMode](./cpnowplayingmode.md)
  A type that defines the appearance and layout of the Now Playing interface.
### Now Playing buttons
- [class CPNowPlayingShuffleButton](./cpnowplayingshufflebutton.md)
  A button for toggling shuffle mode on and off.
- [class CPNowPlayingRepeatButton](./cpnowplayingrepeatbutton.md)
  A button for cycling through the available repeat modes.
- [class CPNowPlayingPlaybackRateButton](./cpnowplayingplaybackratebutton.md)
  A button for changing the playback rate of the media.
- [class CPNowPlayingAddToLibraryButton](./cpnowplayingaddtolibrarybutton.md)
  A button for adding the current item to a collection, such as the person’s library.
- [class CPNowPlayingMoreButton](./cpnowplayingmorebutton.md)
  A button for displaying additional playback options.
- [class CPNowPlayingImageButton](./cpnowplayingimagebutton.md)
  A custom Now Playing button that displays an image.
- [class CPNowPlayingButton](./cpnowplayingbutton.md)
  The abstract base class for buttons in the Now Playing interface.
### Sports mode content
- [class CPNowPlayingSportsTeam](./cpnowplayingsportsteam.md)
  A type that specifies team-specific details, including the name, standings, and current score in the match.
- [class CPNowPlayingSportsTeamLogo](./cpnowplayingsportsteamlogo.md)
  A type that manages logo information for a sports team.
- [class CPNowPlayingSportsEventStatus](./cpnowplayingsportseventstatus.md)
  A type that manages match-focused information, including the event clock.
- [class CPNowPlayingSportsClock](./cpnowplayingsportsclock.md)
  A type that specifies the elapsed or remaining time in a match and the state of the clock.
### Element overlay
- [class CPSportsOverlay](./cpsportsoverlay.md)
  A type that displays sporting event details on top of a thumbnail image.

## See Also

### Now playing
- [class CPNowPlayingTemplate](./cpnowplayingtemplate.md)
  A shared system template that shows the currently selected audio content and offers controls to manage playback.
- [protocol CPNowPlayingTemplateObserver](./cpnowplayingtemplateobserver.md)
  Methods for responding to interactions with buttons in the Now Playing template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/now-playing-support)*